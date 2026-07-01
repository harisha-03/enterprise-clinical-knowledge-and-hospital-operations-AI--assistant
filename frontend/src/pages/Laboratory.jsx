import { FlaskConical, Plus, Clock } from 'lucide-react'
import { Card, CardHeader } from '../components/ui/Card.jsx'
import Button from '../components/ui/Button.jsx'
import DataTable from '../components/tables/DataTable.jsx'
import { labTests } from '../data/mockData.js'

const columns = [
  { key: 'id', label: 'Test ID' },
  { key: 'patient', label: 'Patient' },
  { key: 'test', label: 'Test' },
  { key: 'date', label: 'Date' },
  { key: 'status', label: 'Status' },
]

const statuses = ['Completed', 'Processing', 'Pending']

export default function Laboratory() {
  const pending = labTests.filter((t) => t.status === 'Pending').length
  const processing = labTests.filter((t) => t.status === 'Processing').length
  const completed = labTests.filter((t) => t.status === 'Completed').length

  return (
    <div className="p-6 md:p-8 space-y-6">
      <div className="flex items-center justify-between">
        <div className="flex items-center gap-2.5">
          <div className="w-9 h-9 rounded-lg bg-primary/10 flex items-center justify-center">
            <FlaskConical size={17} className="text-primary-light" />
          </div>
          <div>
            <p className="text-lg font-semibold text-slate-100">Laboratory</p>
            <p className="text-xs text-subtle">Diagnostic test tracking</p>
          </div>
        </div>
        <Button icon={Plus}>New Test Order</Button>
      </div>

      <div className="grid grid-cols-3 gap-4">
        <Card className="p-4">
          <p className="text-xs text-subtle">Completed</p>
          <p className="text-xl font-bold text-success mt-1">{completed}</p>
        </Card>
        <Card className="p-4">
          <p className="text-xs text-subtle">Processing</p>
          <p className="text-xl font-bold text-warning mt-1 flex items-center gap-1.5">
            {processing} <Clock size={14} />
          </p>
        </Card>
        <Card className="p-4">
          <p className="text-xs text-subtle">Pending</p>
          <p className="text-xl font-bold text-danger mt-1">{pending}</p>
        </Card>
      </div>

      <Card>
        <CardHeader title="Test Results" />
        <DataTable columns={columns} data={labTests} searchKeys={['patient', 'test', 'id']} filters={statuses} />
      </Card>
    </div>
  )
}
