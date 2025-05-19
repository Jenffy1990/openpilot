# Parte que debes insertar dentro de la función `update_events(self, CS)`
# justo antes de la línea:
#   # Add FrogPilot events
# o después de esta:
#   if self.sm['modelV2'].frameDropPerc > 20:

model_data = self.sm['modelV2']

# === ALERTAS PERSONALIZADAS DE LUZ, STOP Y VELOCIDAD ===
if hasattr(model_data.meta, "trafficLightState"):
  if model_data.meta.trafficLightState == log.ModelDataV2.MetaData.TrafficLightState.red:
    self.events.add(EventName.redLightDetected)

if hasattr(model_data.meta, "stopLine") and model_data.meta.stopLine:
  self.events.add(EventName.stopSignDetected)

speed_limit = self.sm['frogpilotPlan'].slcSpeedLimit
v_ego = CS.vEgo  # en m/s
if speed_limit > 0 and v_ego > speed_limit + 1.0:
  self.events.add(EventName.speedLimitExceeded)
