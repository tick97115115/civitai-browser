import { expect, test } from 'vitest'
import { ArkErrors, type } from 'arktype'
import { model_types } from '../baseModels/misc'

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

test('enum to list', () => {
  const res = model_types.toJSON() as Array<{ unit: string }>
  console.log(res)
  const arr = []
  for (let index = 0; index < res.length; index++) {
    const element = res[index]
    console.log(element.unit)
    arr.push(element.unit)
  }
  console.log(arr)
  expect(arr[0]).toStrictEqual(res[0].unit)
})
