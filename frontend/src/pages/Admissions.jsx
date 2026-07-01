import { BedDouble, Plus } from 'lucide-react'
import { Card, CardHeader } from '../components/ui/Card.jsx'
import Button from '../components/ui/Button.jsx'
import DataTable from '../components/tables/DataTable.jsx'
import { admissionsList, bedOccupancy } from '../data/mockData.js'

const columns = [
  { key: 'id', label: 'Admission ID' },
  { key: 'patient', label: 'Patient' },
  { key: 'ward', label: 'Ward' },
  { key: 'doctor', label: 'Attending Doctor' },
  { key: 'admittedOn', label: 'Admitted On' },
  { key: 'status', label: 'Status' },
]

const wards = ['ICU', 'General', 'Maternity', 'Pediatric', 'Emergency']

export default function Admissions() {
  return (
    <div className="p-6 md:p-8 space-y-6">
      <div className="flex items-center justify-between">
        <div className="flex items-center gap-2.5">
          <div className="w-9 h-9 rounded-lg bg-primary/10 flex items-center justify-center">
            <BedDouble size={17} className="text-primary-light" />
          </div>
          <div>
            <p className="text-lg font-semibold text-slate-100">{admissionsList.length} Active Records</p>
            <p className="text-xs text-subtle">Ward-wise patient admissions</p>
          </div>
        </div>
        <Button icon={Plus}>New Admission</Button>
      </div>

      <div className="grid grid-cols-2 sm:grid-cols-5 gap-4">
        {bedOccupancy.map((w) => (
          <Card key={w.ward} className="p-4">
            <p className="text-xs text-subtle">{w.ward}</p>
            <p className="text-lg font-bold text-slate-50 mt-1">{w.occupied}<span className="text-sm text-subtle">/{w.total}</span></p>
            <div className="h-1.5 bg-bg rounded-full mt-2 overflow-hidden">
              <div
                className="h-full bg-primary rounded-full"
                style={{ width: `${Math.round((w.occupied / w.total) * 100)}%` }}
              />
            </div>
          </Card>
        ))}
      </div>

      <Card>
        <CardHeader title="Admission Records" />
        <DataTable columns={columns} data={admissionsList} searchKeys={['patient', 'id', 'doctor']} filters={wards} />
      </Card>
    </div>
  )
}
