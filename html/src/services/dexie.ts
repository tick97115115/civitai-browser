import Dexie from 'dexie'

interface ModelVersionTask {
  id: number
  taskId: string
  versionId: number
}

export const db = new Dexie('gopeedTasks') as Dexie & {}
db.version(1).stores({
  tasks: '++id, status',
})
