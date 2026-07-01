import { Users, Plus } from 'lucide-react'
import { Card, CardHeader } from '../components/ui/Card.jsx'
import Button from '../components/ui/Button.jsx'
import DataTable from '../components/tables/DataTable.jsx'
import { patients } from '../data/mockData.js'

const columns = [
  { key: 'id', label: 'Patient ID' },
  { key: 'name', label: 'Name' },
  { key: 'age', label: 'Age' },
  { key: 'gender', label: 'Gender' },
  { key: 'department', label: 'Department' },
  { key: 'lastVisit', label: 'Last Visit' },
  { key: 'status', label: 'Status' },
]

const departments = ['Cardiology', 'Neurology', 'Orthopedics', 'Pediatrics', 'Oncology', 'General']

export default function Patients() {
  return (
    <div className="p-6 md:p-8 space-y-6">
      <div className="flex items-center justify-between">
        <div className="flex items-center gap-2.5">
          <div className="w-9 h-9 rounded-lg bg-primary/10 flex items-center justify-center">
            <Users size={17} className="text-primary-light" />
          </div>
          <div>
            <p className="text-lg font-semibold text-slate-100">{patients.length} Patients</p>
            <p className="text-sm text-subtle">All registered patients across departments</p>
          </div>
        </div>
        <Button icon={Plus}>Add Patient</Button>
      </div>

      <Card>
        <CardHeader title="Patient Records" subtitle="Search, filter, and review patient status" />
        <DataTable columns={columns} data={patients} searchKeys={['name', 'id', 'department']} filters={departments} />
      </Card>
    </div>
  )
}
