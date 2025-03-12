import { type } from 'arktype'
import { versionId_response as versionId_response_from_versionId } from './versionId'
import { creators_response_creator } from './creators'

const models_response_modelVersion = versionId_response_from_versionId.and({
  earlyAccessEndsAt: 'string',
})

export const models_request_period = type("'AllTime' | 'Day' | 'Week' | 'Month' | 'Year'")

const allowCommercialUse = type("'Image' | 'RentCivit' | 'Rent' | 'Sell' | 'None'")
export const models_request_sort = type("'Highest Rated' | 'Most Downloaded' | 'Newest'")

export const model_types = type(
  "'Checkpoint' | 'TextualInversion' | 'Hypernetwork' | 'AestheticGradient' | 'LORA' | 'Controlnet' | 'Poses' | 'LoCon' | 'DoRA' | 'Other' | 'MotionModule' | 'Upscaler' | 'VAE' | 'Wildcards' | 'Workflows'",
)

export const models_response_modelId = type({
  id: 'number.integer',
  name: 'string',
  description: 'string',
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

export const models_response = type({
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

export const models_request_opts = type({
  'limit?': 'number.integer', // The number of results to be returned per page. This can be a number between 1 and 100. By default, each page will return 100 results
  'page?': 'number.integer', // The page from which to start fetching models
  'query?': 'string', // Search query to filter models by name
  'tag?': 'string', // Search query to filter models by tag
  'username?': 'string', // Search query to filter models by user
  'types?': model_types.array(), // The type of model you want to filter with. If none is specified, it will return all types
  'sort?': models_request_sort, // The order in which you wish to sort the results
  'period?': models_request_period, // The time frame in which the models will be sorted
  'rating?': 'number.integer', // The rating you wish to filter the models with. If none is specified, it will return models with any rating
  'favorites?': 'boolean', // (AUTHED) Filter to favorites of the authenticated user (this requires an API token or session cookie)
  'hidden?': 'boolean', // (AUTHED) Filter to hidden models of the authenticated user (this requires an API token or session cookie)
  'primaryFileOnly?': 'boolean', // Only include the primary file for each model (This will use your preferred format options if you use an API token or session cookie)
  'allowNoCredit?': 'boolean', // Filter to models that require or don't require crediting the creator
  'allowDerivatives?': 'boolean', // Filter to models that allow or don't allow creating derivatives
  'allowDifferentLicenses?': 'boolean', // Filter to models that allow or don't allow derivatives to have a different license
  'allowCommercialUse?': allowCommercialUse.array(), // Filter to models based on their commercial permissions
  'nsfw?': 'boolean', // If false, will return safer images and hide models that don't have safe images
  'supportsGeneration?': 'boolean', // If true, will return models that support generation
  'token?': 'string', // required for search models
})

export type ModelsRequestOpts = typeof models_request_opts.infer
