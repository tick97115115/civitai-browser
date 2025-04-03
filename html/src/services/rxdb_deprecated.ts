import { addRxPlugin, createRxDatabase } from 'rxdb/plugins/core'
import type { RxDatabase, RxCollection, RxJsonSchema, RxDocument } from 'rxdb/plugins/core'
import { toTypedRxJsonSchema, type ExtractDocumentTypeFromTypedRxJsonSchema } from 'rxdb'
import { RxDBDevModePlugin } from 'rxdb/plugins/dev-mode'
import { getRxStorageDexie } from 'rxdb/plugins/storage-dexie'
import { wrappedValidateAjvStorage } from 'rxdb/plugins/validate-ajv'
import { object } from 'arktype/internal/attributes.ts'

// const db = await createRxDatabase({
//   name: 'gopeedTasks',
//   storage: getRxStorageDexie(),
// })

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

export type ModelVersionTaskDocMethods = {
  getProgress: () => boolean
  finishAndDelete: () => boolean
}

export type ModelVersionTaskDocument = RxDocument<
  ModelVersionTaskDocType,
  ModelVersionTaskDocMethods
>

// we declare one static ORM-method for the collection
export type ModelVersionTaskCollectionMethods = {
  countAllDocuments: () => Promise<number>
}

// and then merge all our types
export type ModelVersionTaskCollection = RxCollection<
  ModelVersionTaskDocType,
  ModelVersionTaskDocMethods,
  ModelVersionTaskCollectionMethods
>

export type MyDataBaseCollections = {
  modelVersionTasks: ModelVersionTaskCollection
}

export type MyDatabase = RxDatabase<MyDataBaseCollections>

/**
 * create database and collections
 */
const myDataBase: MyDatabase = await createRxDatabase<MyDataBaseCollections>({
  name: 'mydb',
  storage: getRxStorageDexie(),
})

const modelVersionTaskSchema: RxJsonSchema<ModelVersionTaskDocType> = {
  title: 'Gopeed tasks',
  description: 'record model version download tasks those pushed to Gopeed service.',
  version: 0,
  keyCompression: true,
  primaryKey: 'versionId',
  type: 'object',
  properties: {
    versionId: {
      type: 'integer',
    },
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
}

const modelVersionTaskDocMethods: ModelVersionTaskDocMethods = {
  getProgress: function (this: ModelVersionTaskDocument) {
    try {
      // check if task
    } catch (error) {}
  },
}
