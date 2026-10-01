import pyautogui
import pygetwindow as gw
import time

def click_cargar_csv():
    """Encuentra la ventana de Edge con ASMET y hace clic en CARGAR CSV"""
    
    # Buscar ventana de Edge con ASMET
    ventana_asmet = None
    for ventana in gw.getAllWindows():
        if 'edge' in ventana.title.lower() and 'asmet' in ventana.title.lower():
            ventana_asmet = ventana
            break
    
    # Si no encuentra por título completo, buscar solo Edge
    if not ventana_asmet:
        for ventana in gw.getAllWindows():
            if 'edge' in ventana.title.lower():
                ventana_asmet = ventana
                break
    
    if not ventana_asmet:
        print("❌ No se encontró ventana de Edge")
        return False
    
    print(f"✅ Ventana encontrada: {ventana_asmet.title}")
    
    # Activar ventana de Edge
    ventana_asmet.activate()
    time.sleep(2)
    
    # Buscar el botón CARGAR CSV por texto
    try:
        # Buscar botón azul con texto "CARGAR CSV"
        boton = pyautogui.locateOnScreen('cargar_csv', confidence=0.8)
        if boton:
            pyautogui.click(boton)
            print("✅ Clic en CARGAR CSV realizado")
            return True
    except:
        pass
    
    print("❌ No se pudo hacer clic en CARGAR CSV")
    return False

# Ejecutar
if __name__ == "__main__":
    click_cargar_csv()