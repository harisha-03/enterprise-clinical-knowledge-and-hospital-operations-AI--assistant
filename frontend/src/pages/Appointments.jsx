import { CalendarClock, Plus } from 'lucide-react'
import { Card, CardHeader } from '../components/ui/Card.jsx'
import Button from '../components/ui/Button.jsx'
import DataTable from '../components/tables/DataTable.jsx'
import { appointments } from '../data/mockData.js'

const columns = [
  { key: 'id', label: 'Appointment ID' },
  { key: 'patient', label: 'Patient' },
  { key: 'doctor', label: 'Doctor' },
  { key: 'date', label: 'Date' },
  { key: 'time', label: 'Time' },
  { key: 'status', label: 'Status' },
]

const statuses = ['Confirmed', 'Pending', 'Completed', 'Cancelled']

export default function Appointments() {
  return (
    <div className="p-6 md:p-8 space-y-6">
      <div className="flex items-center justify-between">
        <div className="flex items-center gap-2.5">
          <div className="w-9 h-9 rounded-lg bg-primary/10 flex items-center justify-center">
            <CalendarClock size={17} className="text-primary-light" />
          </div>
          <div>
            <p className="text-lg font-semibold text-slate-100">{appointments.length} Appointments</p>
            <p className="text-xs text-subtle">Upcoming and recent scheduling</p>
          </div>
        </div>
        <Button icon={Plus}>New Appointment</Button>
      </div>

      <Card>
        <CardHeader title="Appointment Schedule" />
        <DataTable columns={columns} data={appointments} searchKeys={['patient', 'doctor', 'id']} filters={statuses} />
      </Card>
    </div>
  )
}
