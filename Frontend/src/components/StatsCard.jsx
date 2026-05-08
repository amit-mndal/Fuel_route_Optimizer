export default function StatsCard({ title, value }) {
  return (
    <div className="bg-slate-800 p-5 rounded-2xl shadow-lg">
      <p className="text-slate-400 text-sm">{title}</p>

      <h2 className="text-2xl font-bold mt-2">{value}</h2>
    </div>
  );
}