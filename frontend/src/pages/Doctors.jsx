import { Stethoscope, Star, Plus } from 'lucide-react'
import { Card, CardHeader } from '../components/ui/Card.jsx'
import Button from '../components/ui/Button.jsx'
import Badge, { statusVariant } from '../components/ui/Badge.jsx'
import DataTable from '../components/tables/DataTable.jsx'
import { doctors } from '../data/mockData.js'

const departments = ['Cardiology', 'Neurology', 'Orthopedics', 'Pediatrics', 'Oncology', 'General']

const columns = [
  { key: 'id', label: 'Doctor ID' },
  { key: 'name', label: 'Name' },
  { key: 'department', label: 'Department' },
  { key: 'patients', label: 'Patients' },
  {
    key: 'rating',
    label: 'Rating',
    render: (row) => (
      <span className="flex items-center gap-1">
        <Star size={12} className="text-warning fill-warning" /> {row.rating}
      </span>
    ),
  },
  { key: 'status', label: 'Status' },
]

export default function Doctors() {
  return (
    <div className="p-6 md:p-8 space-y-6">
      <div className="flex items-center justify-between">
        <div className="flex items-center gap-2.5">
          <div className="w-9 h-9 rounded-lg bg-primary/10 flex items-center justify-center">
            <Stethoscope size={17} className="text-primary-light" />
          </div>
          <div>
            <p className="text-lg font-semibold text-slate-100">{doctors.length} Doctors</p>
            <p className="text-xs text-subtle">Medical staff across all departments</p>
          </div>
        </div>
        <Button icon={Plus}>Add Doctor</Button>
      </div>

      <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4">
        {doctors.slice(0, 4).map((doc) => (
          <Card key={doc.id} hover className="p-4">
            <div className="flex items-center gap-3">
              <div className="w-10 h-10 rounded-full bg-gradient-to-br from-primary to-primary-dark flex items-center justify-center text-xs font-semibold text-white shrink-0">
                {doc.name.split(' ').slice(-2).map((p) => p[0]).join('')}
              </div>
              <div className="min-w-0">
                <p className="text-sm font-medium text-slate-100 truncate">{doc.name}</p>
                <p className="text-xs text-subtle truncate">{doc.department}</p>
              </div>
            </div>
            <div className="flex items-center justify-between mt-3">
              <Badge variant={statusVariant(doc.status)}>{doc.status}</Badge>
              <span className="flex items-center gap-1 text-xs text-warning">
                <Star size={11} className="fill-warning" /> {doc.rating}
              </span>
            </div>
          </Card>
        ))}
      </div>

      <Card>
        <CardHeader title="All Doctors" subtitle="Filter by department or availability" />
        <DataTable columns={columns} data={doctors} searchKeys={['name', 'id', 'department']} filters={departments} />
      </Card>
    </div>
  )
}
