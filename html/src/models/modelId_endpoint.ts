import { modelVersion_Base } from './baseModels/modelVersion'
import { model_types, allowCommercialUse } from './baseModels/misc'
import { type } from 'arktype'

export const modelId_endpoint_modelVersion = modelVersion_Base.and({
  availability: "'EarlyAccess' | 'Public'",
  // covered: 'boolean', // have cover image or not
  index: 'number.integer', // the position in modelId.modelVersions array.
  nsfwLevel: 'number.integer',
})
export type ModelIdEndpointModelVersion = typeof modelId_endpoint_modelVersion.infer

import { creators_response_creator } from './creators_endpoint'
// https://www.jsondiff.com/ 找到共有属性名

export const modelId_response = type({
  id: 'number.integer',
  name: 'string',
  description: 'string | null',
  allowNoCredit: 'boolean',
  allowCommercialUse: allowCommercialUse.array(),
  allowDerivatives: 'boolean',
  allowDifferentLicense: 'boolean',
  type: model_types,
  minor: 'boolean',
  poi: 'boolean',
  nsfw: 'boolean',
  nsfwLevel: 'number.integer',
  tags: 'string[]',
  'creator?': creators_response_creator,
  stats: {
    downloadCount: 'number.integer',
    favoriteCount: 'number.integer',
    thumbsUpCount: 'number.integer',
    thumbsDownCount: 'number.integer',
    commentCount: 'number.integer',
    ratingCount: 'number.integer',
    rating: 'number',
    tippedAmountCount: 'number.integer',
  },
  modelVersions: modelId_endpoint_modelVersion.array(),
})
export type ModelIdResponse = typeof modelId_response.infer
