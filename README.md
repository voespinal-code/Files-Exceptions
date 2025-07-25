# Python Crash Course · Capítulo 10 · Files & Exceptions

Scripts que practican lectura/escritura de archivos y manejo de excepciones.

| Script | Descripción | Cómo ejecutar |
|--------|-------------|---------------|
| `learning_python.py` | Imprime líneas favoritas sobre Python. | `python src/learning_python.py` |
| `learning_c.py` | Sustituye la palabra *Python* por *C* en las líneas. | `python src/learning_c.py` |
| `guess_number.py` | Juego de adivinar número con manejo de `ValueError`. | `python src/guess_number.py` |
| `file_reader.py` | Abre un archivo y gestiona `FileNotFoundError`. | `python src/file_reader.py data/pi_digits.txt` |
| `message_writer.py` | Guarda un input del usuario en un fichero. | `python src/message_writer.py` |
| `pi_birthday.py` | Comprueba si tu cumple está en los dígitos de π. | `python src/pi_birthday.py data/pi_digits.txt` |

## Requisitos
```bash
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt  # vacío por ahora
