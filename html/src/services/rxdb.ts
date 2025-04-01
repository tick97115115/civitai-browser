import { addRxPlugin, createRxDatabase } from 'rxdb/plugins/core'
import type { RxDatabase, RxCollection, RxJsonSchema, RxDocument } from 'rxdb/plugins/core'
import { toTypedRxJsonSchema, type ExtractDocumentTypeFromTypedRxJsonSchema } from 'rxdb'
import { RxDBDevModePlugin } from 'rxdb/plugins/dev-mode'
import { getRxStorageDexie } from 'rxdb/plugins/storage-dexie'
import { wrappedValidateAjvStorage } from 'rxdb/plugins/validate-ajv'

const db = await createRxDatabase({
  name: 'gopeedTasks',
  storage: getRxStorageDexie(),
})

// For dev
// addRxPlugin(RxDBDevModePlugin);

export const tasksSchemaLiteral: RxJsonSchema<any> = {
  version: 0,
  type: 'object',
  primaryKey: 'taskId',
  properties: {
    versionId: { type: 'integer' },
    taskId: { type: 'string', maxLength: 100 },
    relatedImgsTasks: {
      type: 'array',
      uniqueItems: true,
      items: {
        type: 'string',
      },
    },
  },
  required: ['taskId', 'relatedImgsTasks'],
  indexes: ['versionId'],
} as const
const tasksSchemaTyped = toTypedRxJsonSchema(tasksSchemaLiteral)

export type ModelVersionTaskDocType = ExtractDocumentTypeFromTypedRxJsonSchema<
  typeof tasksSchemaTyped
>
export const tasksSchema: RxJsonSchema<ModelVersionTaskDocType> = tasksSchemaLiteral
