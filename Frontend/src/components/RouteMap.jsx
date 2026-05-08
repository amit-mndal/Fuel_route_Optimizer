import { MapContainer, TileLayer, Polyline } from "react-leaflet";
import "leaflet/dist/leaflet.css";
import polyline from "@mapbox/polyline";

export default function RouteMap({ geometry }) {
  if (!geometry) return null;

  const decoded = polyline.decode(geometry);

  return (
    <div className="rounded-2xl overflow-hidden shadow-lg">
      <MapContainer
        center={decoded[0]}
        zoom={5}
        style={{ height: "500px", width: "100%" }}
      >
        <TileLayer
          attribution='&copy; OpenStreetMap contributors'
          url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
        />

        <Polyline positions={decoded} />
      </MapContainer>
    </div>
  );
}