import { type } from 'arktype'

export const creators_response_creator = type({
  username: 'string',
  'modelCount?': 'number.integer',
  'link?': 'string.url',
  'image?': 'string.url',
})

const creators_response = type({
  items: creators_response_creator.array(),
  metadata: {
    totalItems: 'number.integer',
    currentPage: 'number.integer',
    pageSize: 'number.integer',
    totalPages: 'number.integer',
    'nextPage?': 'string.url',
    'prevPage?': 'string.url',
  },
})

const creators_request_opts = type({
  'limit?': 'number.integer',
  'page?': 'number.integer',
  'query?': 'string',
})
