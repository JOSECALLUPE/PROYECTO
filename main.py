import cv2

def main():
    print("Iniciando aplicación OpenCV.")
    # Crea una imagen en blanco para la demostración si no tienes una
    img = cv2.imread('imagen_ejemplo.jpg') # Asegúrate de tener una imagen llamada imagen_ejemplo.jpg en la misma carpeta

    if img is None:
        print("No se pudo cargar la imagen. Creando una imagen de ejemplo en blanco.")
        img = 255 * (200, 300, 3) # Imagen en blanco de 200x300 pixels
        cv2.putText(img, "Hola OpenCV!", (50, 150), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2, cv2.LINE_AA)

    cv2.imshow('Imagen Original', img)
    print("Presiona cualquier tecla para salir.")
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
git add main.py
git commit -m "Add Canny edge detection to main.py"
git push origin master # O git push origin main si tu rama es main
