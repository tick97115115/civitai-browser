import { addRxPlugin, createRxDatabase } from 'rxdb/plugins/core'
import { getRxStorageDexie } from 'rxdb/plugins/storage-dexie'
import { getRxStorageLocalstorage } from 'rxdb/plugins/storage-localstorage'
import { wrappedValidateAjvStorage } from 'rxdb/plugins/validate-ajv'

const db = await createRxDatabase({
  name: 'exampledb',
  storage: getRxStorageDexie(),
})

await db.addCollections({
  tasks: {
    schema: {
      title: 'Gopeed tasks',
      version: 0,
      primaryKey: 'versionId',
      type: 'object',
      properties: {
        versionId: { type: 'integer' },
        modelFilesUrls: { type: 'array', items: { type: 'string' } },
        modelVersionImgsUrls: { type: 'array', items: { type: 'string' } },
        done: { type: 'boolean' },
      },
      required: ['versionId', 'modelFilesUrls', 'done'],
      indexes: ['versionId'],
    },
  },
})
