export default function FuelStops({ stops }) {
  return (
    <div className="bg-slate-800 p-6 rounded-2xl shadow-lg">
      <h2 className="text-xl font-bold mb-4">Fuel Stops</h2>

      <div className="space-y-4">
        {stops.map((stop, index) => (
          <div
            key={index}
            className="bg-slate-700 p-4 rounded-xl"
          >
            <h3 className="font-semibold text-lg">
              {stop.truckstop_name}
            </h3>

            <p>
              {stop.city}, {stop.state}
            </p>

            <p>
              Price/Gallon: ${stop.price_per_gallon}
            </p>

            <p>
              Fuel Cost: ${stop.estimated_fuel_cost}
            </p>
          </div>
        ))}
      </div>
    </div>
  );
}