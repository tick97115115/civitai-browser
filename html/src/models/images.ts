import { type } from 'arktype'

const nsfwLevel = type("'None' | 'Soft' | 'Mature' | 'X'")

const images_response_item = type({
  id: 'number.integer',
  url: 'string.url',
  hash: 'string',
  height: 'number.integer',
  nsfw: 'boolean',
  nsfwLevel: nsfwLevel,
  createdAt: 'string',
  postId: 'number.integer',
  stats: {
    cryCount: 'number.integer',
    laughCount: 'number.integer',
    likeCount: 'number.integer',
    heartCount: 'number.integer',
    commentCount: 'number.integer',
  },
  meta: 'object',
  'username?': 'string',
  'baseModel?': 'string',
})

const images_response = type({
  items: images_response_item.array(),
  metadata: {
    'nextCursor?': 'number.integer',
    'currentPage?': 'number.integer',
    'pageSize?': 'number.integer',
    'nextPage?': 'string.url',
  },
})
