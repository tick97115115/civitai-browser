import { modelVersion_Base } from './baseModels/modelVersion'
import { model_types, modelVersion_Base_image } from './baseModels/misc'

export const versionId_endpoint_modelVersion = modelVersion_Base.and({
  air: 'string',
  baseModelType: 'string | null',
  description: 'string | null',
  earlyAccessConfig: {
    timeframe: 'number.integer',
    donationGoal: 'number.integer',
    downloadPrice: 'number.integer',
    donationGoalId: 'number.integer',
    generationPrice: 'number.integer',
    chargeForDownload: 'boolean',
    chargeForGeneration: 'boolean',
    donationGoalEnabled: 'boolean',
    originalPublishedAt: 'string', // ISO8061
    generationTrialLimit: 'number.integer',
  },
  earlyAccessEndsAt: 'string', // ISO8061
  model: {
    name: 'string',
    nsfw: 'boolean',
    poi: 'boolean',
    type: model_types,
  },
  modelId: 'number',
  updatedAt: 'string', // ISO 8061
  uploadType: 'string', // This looks like an enum type
  usageControl: 'string', // This looks like an enum type
  images: modelVersion_Base_image
    .and({
      metadata: {
        hash: 'string',
        height: 'number.integer',
        size: 'number.integer',
        width: 'number.integer',
      },
    })
    .array(),
})

// type test = typeof versionId_endpoint_modelVersion.infer

// // @ts-ignore
// const a : test = {}

// a.images[0].metadata
