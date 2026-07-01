import { Users, Stethoscope, CalendarClock, BedDouble, IndianRupee, Activity } from 'lucide-react'
import {
  AreaChart, Area, LineChart, Line, BarChart, Bar, PieChart, Pie, Cell,
  XAxis, YAxis, CartesianGrid, Tooltip, ResponsiveContainer, Legend,
} from 'recharts'
import KpiCard from '../components/dashboard/KpiCard.jsx'
import ChartShell, { chartTooltipStyle } from '../components/charts/ChartShell.jsx'
import { Card, CardHeader } from '../components/ui/Card.jsx'
import {
  kpis, admissionsTrend, revenueTrend, departmentDistribution, bedOccupancy, recentActivity,
} from '../data/mockData.js'

const activityDotColor = {
  admission: 'bg-success',
  discharge: 'bg-primary',
  lab: 'bg-warning',
  appointment: 'bg-primary-light',
  billing: 'bg-subtle',
}

export default function Dashboard() {
  return (
    <div className="p-6 md:p-8 space-y-7">
      <div className="grid grid-cols-2 lg:grid-cols-3 xl:grid-cols-6 gap-6">
        <KpiCard label="Patients" value={kpis.patients.value} delta={kpis.patients.delta} icon={Users} />
        <KpiCard label="Doctors" value={kpis.doctors.value} delta={kpis.doctors.delta} icon={Stethoscope} />
        <KpiCard label="Appointments" value={kpis.appointments.value} delta={kpis.appointments.delta} icon={CalendarClock} />
        <KpiCard label="Admissions" value={kpis.admissions.value} delta={kpis.admissions.delta} icon={Activity} />
        <KpiCard
          label="Revenue"
          value={kpis.revenue.value}
          delta={kpis.revenue.delta}
          icon={IndianRupee}
          prefix="₹"
          format={(v) => (v / 100000).toFixed(1) + 'L'}
        />
        <KpiCard
          label="Beds Occupied"
          value={kpis.beds.occupied}
          icon={BedDouble}
          suffix={` / ${kpis.beds.value}`}
        />
      </div>

      <div className="grid grid-cols-1 lg:grid-cols-3 gap-6">
        <ChartShell title="Admissions Trend" subtitle="Monthly admissions vs discharges" className="lg:col-span-2">
          <ResponsiveContainer width="100%" height={260}>
            <AreaChart data={admissionsTrend} margin={{ left: -16, right: 8 }}>
              <defs>
                <linearGradient id="admGrad" x1="0" y1="0" x2="0" y2="1">
                  <stop offset="0%" stopColor="#2563EB" stopOpacity={0.35} />
                  <stop offset="100%" stopColor="#2563EB" stopOpacity={0} />
                </linearGradient>
              </defs>
              <CartesianGrid strokeDasharray="3 3" stroke="#1F2937" vertical={false} />
              <XAxis dataKey="month" stroke="#64748B" fontSize={12} tickLine={false} axisLine={false} />
              <YAxis stroke="#64748B" fontSize={12} tickLine={false} axisLine={false} />
              <Tooltip {...chartTooltipStyle} />
              <Legend wrapperStyle={{ fontSize: 12, color: '#94A3B8' }} />
              <Area type="monotone" dataKey="admissions" stroke="#2563EB" fill="url(#admGrad)" strokeWidth={2} name="Admissions" />
              <Line type="monotone" dataKey="discharges" stroke="#10B981" strokeWidth={2} dot={false} name="Discharges" />
            </AreaChart>
          </ResponsiveContainer>
        </ChartShell>

        <ChartShell title="Department Distribution" subtitle="Active cases by department">
          <ResponsiveContainer width="100%" height={260}>
            <PieChart>
              <Pie
                data={departmentDistribution}
                dataKey="value"
                nameKey="name"
                innerRadius={55}
                outerRadius={85}
                paddingAngle={3}
              >
                {departmentDistribution.map((d) => (
                  <Cell key={d.name} fill={d.color} stroke="none" />
                ))}
              </Pie>
              <Tooltip {...chartTooltipStyle} />
              <Legend
                layout="vertical"
                align="right"
                verticalAlign="middle"
                wrapperStyle={{ fontSize: 11, color: '#94A3B8' }}
              />
            </PieChart>
          </ResponsiveContainer>
        </ChartShell>
      </div>

      <div className="grid grid-cols-1 lg:grid-cols-3 gap-6">
        <ChartShell title="Revenue Trend" subtitle="Revenue vs operating expenses (₹)" className="lg:col-span-2">
          <ResponsiveContainer width="100%" height={250}>
            <LineChart data={revenueTrend} margin={{ left: -16, right: 8 }}>
              <CartesianGrid strokeDasharray="3 3" stroke="#1F2937" vertical={false} />
              <XAxis dataKey="month" stroke="#64748B" fontSize={12} tickLine={false} axisLine={false} />
              <YAxis
                stroke="#64748B"
                fontSize={12}
                tickLine={false}
                axisLine={false}
                tickFormatter={(v) => `${(v / 100000).toFixed(0)}L`}
              />
              <Tooltip {...chartTooltipStyle} formatter={(v) => `₹${v.toLocaleString('en-IN')}`} />
              <Legend wrapperStyle={{ fontSize: 12, color: '#94A3B8' }} />
              <Line type="monotone" dataKey="revenue" stroke="#2563EB" strokeWidth={2.5} dot={false} name="Revenue" />
              <Line type="monotone" dataKey="expenses" stroke="#F59E0B" strokeWidth={2} dot={false} name="Expenses" />
            </LineChart>
          </ResponsiveContainer>
        </ChartShell>

        <ChartShell title="Bed Occupancy" subtitle="By ward">
          <ResponsiveContainer width="100%" height={250}>
            <BarChart data={bedOccupancy} layout="vertical" margin={{ left: 8, right: 16 }}>
              <CartesianGrid strokeDasharray="3 3" stroke="#1F2937" horizontal={false} />
              <XAxis type="number" stroke="#64748B" fontSize={11} tickLine={false} axisLine={false} />
              <YAxis dataKey="ward" type="category" stroke="#94A3B8" fontSize={11} tickLine={false} axisLine={false} width={70} />
              <Tooltip {...chartTooltipStyle} />
              <Bar dataKey="total" fill="#1F2937" radius={[0, 4, 4, 0]} name="Total beds" />
              <Bar dataKey="occupied" fill="#2563EB" radius={[0, 4, 4, 0]} name="Occupied" />
            </BarChart>
          </ResponsiveContainer>
        </ChartShell>
      </div>

      <Card>
        <CardHeader title="Recent Activity" subtitle="Latest events across the hospital" />
        <div className="px-6 pb-6 divide-y divide-border">
          {recentActivity.map((item) => (
            <div key={item.id} className="flex items-center gap-3.5 py-3.5">
              <span className={`w-2.5 h-2.5 rounded-full ${activityDotColor[item.type] || 'bg-subtle'}`} />
              <p className="text-[15px] text-slate-300 flex-1">{item.text}</p>
              <span className="text-sm text-subtle whitespace-nowrap">{item.time}</span>
            </div>
          ))}
        </div>
      </Card>
    </div>
  )
}
