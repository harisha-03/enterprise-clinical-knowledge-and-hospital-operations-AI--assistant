import { Receipt, IndianRupee, TrendingUp, AlertCircle } from 'lucide-react'
import { AreaChart, Area, CartesianGrid, XAxis, YAxis, Tooltip, ResponsiveContainer } from 'recharts'
import { Card, CardHeader } from '../components/ui/Card.jsx'
import ChartShell, { chartTooltipStyle } from '../components/charts/ChartShell.jsx'
import DataTable from '../components/tables/DataTable.jsx'
import KpiCard from '../components/dashboard/KpiCard.jsx'
import { invoices, revenueTrend } from '../data/mockData.js'

const columns = [
  { key: 'id', label: 'Invoice ID' },
  { key: 'patient', label: 'Patient' },
  { key: 'date', label: 'Date' },
  {
    key: 'amount',
    label: 'Amount',
    render: (row) => `₹${row.amount.toLocaleString('en-IN')}`,
  },
  { key: 'status', label: 'Status' },
]

const statuses = ['Paid', 'Pending', 'Overdue']

export default function Billing() {
  const totalRevenue = invoices.reduce((sum, i) => sum + (i.status !== 'Overdue' ? i.amount : 0), 0)
  const overdue = invoices.filter((i) => i.status === 'Overdue').reduce((sum, i) => sum + i.amount, 0)
  const pendingCount = invoices.filter((i) => i.status === 'Pending').length

  return (
    <div className="p-6 md:p-8 space-y-6">
      <div className="flex items-center gap-2.5">
        <div className="w-9 h-9 rounded-lg bg-primary/10 flex items-center justify-center">
          <Receipt size={17} className="text-primary-light" />
        </div>
        <div>
          <p className="text-lg font-semibold text-slate-100">Billing &amp; Revenue</p>
          <p className="text-xs text-subtle">Invoices, payments and outstanding balances</p>
        </div>
      </div>

      <div className="grid grid-cols-1 sm:grid-cols-3 gap-4">
        <KpiCard label="Total Collected" value={totalRevenue} icon={IndianRupee} prefix="₹" format={(v) => v.toLocaleString('en-IN')} />
        <KpiCard label="Pending Invoices" value={pendingCount} icon={TrendingUp} />
        <KpiCard label="Overdue Amount" value={overdue} icon={AlertCircle} prefix="₹" format={(v) => v.toLocaleString('en-IN')} />
      </div>

      <ChartShell title="Revenue Overview" subtitle="Monthly collections (₹)">
        <ResponsiveContainer width="100%" height={240}>
          <AreaChart data={revenueTrend} margin={{ left: -16, right: 8 }}>
            <defs>
              <linearGradient id="revGrad" x1="0" y1="0" x2="0" y2="1">
                <stop offset="0%" stopColor="#10B981" stopOpacity={0.3} />
                <stop offset="100%" stopColor="#10B981" stopOpacity={0} />
              </linearGradient>
            </defs>
            <CartesianGrid strokeDasharray="3 3" stroke="#1F2937" vertical={false} />
            <XAxis dataKey="month" stroke="#64748B" fontSize={12} tickLine={false} axisLine={false} />
            <YAxis stroke="#64748B" fontSize={12} tickLine={false} axisLine={false} tickFormatter={(v) => `${(v / 100000).toFixed(0)}L`} />
            <Tooltip {...chartTooltipStyle} formatter={(v) => `₹${v.toLocaleString('en-IN')}`} />
            <Area type="monotone" dataKey="revenue" stroke="#10B981" fill="url(#revGrad)" strokeWidth={2.5} name="Revenue" />
          </AreaChart>
        </ResponsiveContainer>
      </ChartShell>

      <Card>
        <CardHeader title="Invoices" />
        <DataTable columns={columns} data={invoices} searchKeys={['patient', 'id']} filters={statuses} />
      </Card>
    </div>
  )
}
