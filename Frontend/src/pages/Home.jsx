import { useState } from "react";
import FuelStops from "../components/FuelStops";
import RouteMap from "../components/RouteMap";
import RouteForm from "../components/RouteForm";
import StatsCard from "../components/StatsCard";

import { optimizeRoute } from "../services/api";

export default function Home() {
  const [data, setData] = useState(null);
  const [loading, setLoading] = useState(false);

  const handleOptimize = async (formData) => {
    try {
      setLoading(true);

      const response = await optimizeRoute(formData);

      setData(response);

    } catch (error) {
      console.log(error);
      alert("Something went wrong");

    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="max-w-7xl mx-auto p-6 space-y-6">

      <RouteForm
        onSubmit={handleOptimize}
        loading={loading}
      />

      {data && (
        <>
          <div className="grid md:grid-cols-3 gap-4">

            <StatsCard
              title="Distance"
              value={`${data.distance_miles} miles`}
            />

            <StatsCard
              title="Fuel Cost"
              value={`$${data.total_fuel_cost}`}
            />

            <StatsCard
              title="Fuel Stops"
              value={data.fuel_stops.length}
            />
          </div>

          <RouteMap geometry={data.route_geometry} />

          <FuelStops stops={data.fuel_stops} />
        </>
      )}
    </div>
  );
}