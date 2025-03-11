import { type } from 'arktype'
import { versionId_response as versionId_response_from_versionId } from './versionId'
import { creators_response_creator } from './creators'

const models_response_modelVersion = versionId_response_from_versionId.and({
  earlyAccessEndsAt: 'string',
})

const models_response_modelId = type({
  id: 'number.integer',
  name: 'string',
  description: 'string',
  allowNoCredit: 'boolean',
  allowCommercialUse: '("Image" | "RentCivit" | "Rent" | "Sell" | "None")[]',
  allowDerivatives: 'boolean',
  allowDifferentLicense: 'boolean',
  type: "'Checkpoint' | 'TextualInversion' | 'Hypernetwork' | 'AestheticGradient' | 'LORA' | 'Controlnet' | 'Poses' | 'LoCon' | 'DoRA' | 'Other' | 'MotionModule' | 'Upscaler' | 'VAE' | 'Wildcards' | 'Workflows'",
  minor: 'boolean',
  poi: 'boolean',
  nsfw: 'boolean',
  nsfwLevel: 'number.integer',
  tags: 'string[]',
  creator: creators_response_creator,
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
  modelVersions: models_response_modelVersion.array(),
})

const models_response = type({
  items: models_response_modelId.array(),
  metadata: {
    'totalItems?': 'number.integer',
    'currentPage?': 'number.integer',
    'pageSize?': 'number.integer',
    'totalPages?': 'number.integer',
    'nextPage?': 'string.url',
    'prevPage?': 'string.url',
  },
})
