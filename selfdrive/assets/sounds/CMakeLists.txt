# selfdrive/assets/sounds/CMakeLists.txt

# Agrupa todos los .wav en esta carpeta
file(GLOB ASSETS "*.wav")

# Le dice al build system de OpenPilot que empaquete estos archivos
openpilot_add_assets("selfdrive/assets/sounds" "${ASSETS}")
