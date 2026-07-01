import { BarChart3 } from 'lucide-react'
import {
  ComposedChart, Bar, Line, BarChart, RadarChart, PolarGrid, PolarAngleAxis, PolarRadiusAxis, Radar,
  CartesianGrid, XAxis, YAxis, Tooltip, ResponsiveContainer, Legend,
} from 'recharts'
import ChartShell, { chartTooltipStyle } from '../components/charts/ChartShell.jsx'
import { admissionsTrend, revenueTrend, departmentDistribution, bedOccupancy } from '../data/mockData.js'

const radarData = departmentDistribution.map((d) => ({ department: d.name, load: d.value }))

export default function Analytics() {
  return (
    <div className="p-6 md:p-8 space-y-6">
      <div className="flex items-center gap-2.5">
        <div className="w-9 h-9 rounded-lg bg-primary/10 flex items-center justify-center">
          <BarChart3 size={17} className="text-primary-light" />
        </div>
        <div>
          <p className="text-sm font-semibold text-slate-100">Analytics</p>
          <p className="text-xs text-subtle">Operational performance across the hospital</p>
        </div>
      </div>

      <div className="grid grid-cols-1 lg:grid-cols-2 gap-5">
        <ChartShell title="Admissions vs Revenue" subtitle="Correlated monthly performance">
          <ResponsiveContainer width="100%" height={280}>
            <ComposedChart data={admissionsTrend.map((a, i) => ({ ...a, revenue: revenueTrend[i]?.revenue }))} margin={{ left: -10, right: 10 }}>
              <CartesianGrid strokeDasharray="3 3" stroke="#1F2937" vertical={false} />
              <XAxis dataKey="month" stroke="#64748B" fontSize={12} tickLine={false} axisLine={false} />
              <YAxis yAxisId="left" stroke="#64748B" fontSize={11} tickLine={false} axisLine={false} />
              <YAxis yAxisId="right" orientation="right" stroke="#64748B" fontSize={11} tickLine={false} axisLine={false} tickFormatter={(v) => `${(v / 100000).toFixed(0)}L`} />
              <Tooltip {...chartTooltipStyle} />
              <Legend wrapperStyle={{ fontSize: 12, color: '#94A3B8' }} />
              <Bar yAxisId="left" dataKey="admissions" fill="#2563EB" radius={[4, 4, 0, 0]} name="Admissions" />
              <Line yAxisId="right" type="monotone" dataKey="revenue" stroke="#10B981" strokeWidth={2.5} dot={false} name="Revenue (₹)" />
            </ComposedChart>
          </ResponsiveContainer>
        </ChartShell>

        <ChartShell title="Department Load" subtitle="Relative case volume by department">
          <ResponsiveContainer width="100%" height={280}>
            <RadarChart data={radarData}>
              <PolarGrid stroke="#1F2937" />
              <PolarAngleAxis dataKey="department" stroke="#94A3B8" fontSize={11} />
              <PolarRadiusAxis stroke="#1F2937" fontSize={10} />
              <Radar dataKey="load" stroke="#2563EB" fill="#2563EB" fillOpacity={0.35} />
              <Tooltip {...chartTooltipStyle} />
            </RadarChart>
          </ResponsiveContainer>
        </ChartShell>
      </div>

      <ChartShell title="Bed Occupancy Efficiency" subtitle="Occupied vs available capacity by ward">
        <ResponsiveContainer width="100%" height={260}>
          <BarChart data={bedOccupancy} margin={{ left: -10, right: 10 }}>
            <CartesianGrid strokeDasharray="3 3" stroke="#1F2937" vertical={false} />
            <XAxis dataKey="ward" stroke="#64748B" fontSize={12} tickLine={false} axisLine={false} />
            <YAxis stroke="#64748B" fontSize={12} tickLine={false} axisLine={false} />
            <Tooltip {...chartTooltipStyle} />
            <Legend wrapperStyle={{ fontSize: 12, color: '#94A3B8' }} />
            <Bar dataKey="total" fill="#1F2937" radius={[4, 4, 0, 0]} name="Total Beds" />
            <Bar dataKey="occupied" fill="#2563EB" radius={[4, 4, 0, 0]} name="Occupied" />
          </BarChart>
        </ResponsiveContainer>
      </ChartShell>
    </div>
  )
}
