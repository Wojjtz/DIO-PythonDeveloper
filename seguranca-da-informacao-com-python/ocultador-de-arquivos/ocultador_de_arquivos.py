import ctypes

# define o atributo do arquivo a ser ocultado (hexadecimal)
atributo_ocultar = 0x02

# responsável por ocultar o arquivo 
retorno = ctypes.windll.kernel32.SetFileAttributesW('seguranca-da-informacao-com-python/ocultador-de-arquivos/ocultar.txt', atributo_ocultar)

if retorno:
    print("Arquivo ocultado.")
else: 
    print("Arquivo não foi ocultado.")

# é possível ocultar pastas