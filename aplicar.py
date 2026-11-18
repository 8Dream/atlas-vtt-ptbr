#!/usr/bin/env python3
"""Aplica a traducao PT-BR ao plugin Atlas VTT (Obsidian) ja instalado.

Uso:  python aplicar.py "<pasta do plugin>"      (a pasta que contem main.js)
      python aplicar.py "<pasta do plugin>" --desfazer

Nao inclui nem distribui o plugin: so altera a copia que voce ja tem.
Guarda o original em main.js.original antes de alterar.
"""
import json
import re
import shutil
import sys
from pathlib import Path

AQUI = Path(__file__).resolve().parent
PADRAO = re.compile(r"\{en:(\w+),ru:(\w+),zh:(\w+)\}")


def main() -> int:
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    desfazer = "--desfazer" in sys.argv
    if len(args) != 1:
        print(__doc__)
        return 2
    pasta = Path(args[0])
    js, original = pasta / "main.js", pasta / "main.js.original"
    if not js.is_file():
        print(f"main.js nao encontrado em {pasta}")
        return 1

    if desfazer:
        if not original.is_file():
            print("Nao ha main.js.original: nada a desfazer.")
            return 1
        shutil.copyfile(original, js)
        print("Original restaurado.")
        return 0

    texto = js.read_text(encoding="utf-8")
    if "Analisando o mapa" in texto:
        print("Ja traduzido. Para reaplicar sobre uma versao nova, atualize o plugin e rode de novo.")
        return 0
    achados = PADRAO.findall(texto)
    if len(achados) != 1:
        print(f"Esperava 1 objeto de idiomas {{en:..,ru:..,zh:..}} e achei {len(achados)}. "
              "Esta versao do plugin mudou; a traducao precisa ser adaptada.")
        return 1
    traducao = json.loads((AQUI / "traducao-pt-BR.json").read_text(encoding="utf-8"))
    pt = json.dumps(traducao, ensure_ascii=False, separators=(",", ":"))
    en, ru, zh = achados[0]
    novo = "{en:Object.assign(%s,%s),pt:%s,ru:%s,zh:%s}" % (en, pt, en, ru, zh)
    if not original.exists():
        shutil.copyfile(js, original)
    js.write_text(PADRAO.sub(lambda _m: novo, texto, count=1), encoding="utf-8", newline="")
    print(f"Traducao aplicada ({len(traducao)} textos). Reinicie o Obsidian.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
