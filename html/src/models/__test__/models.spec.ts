import { expect, test } from 'vitest'
import { ArkErrors, type } from 'arktype'

test('enum', () => {
  const enumerate_type = type({
    sort: "('Newest' | 'Oldest')[]",
    username: 'string',
  })
  type EnumerateType = typeof enumerate_type.infer

  const instance = enumerate_type({ sort: ['Unknown'] })
  if (instance instanceof type.errors) {
    // hover out.summary to see validation errors
    console.log(instance.toTraversalError().message)
    instance.throw()
  } else {
    // hover out to see your validated data
    console.log(`Hello, ${instance.sort}`)
  }
  expect(instance.sort).toStrictEqual('Oldest')
})
