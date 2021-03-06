def init():
  return """
  {
    "queryType": "select",
    "dataSource": "content-model-snapshot",
    "filter": {
      "type": "and",
      "fields": [
        {
          "type": "selector",
          "dimension": "contentType",
          "value": "Course"
        },
        {
          "type": "selector",
          "dimension": "status",
          "value": "Live"
        }
      ]
    },
    "aggregations": [],
    "granularity": "all",
    "postAggregations": [],
    "intervals": "1901-01-01T00:00:00+00:00/2101-01-01T00:00:00+00:00",
    "dimensions": [
      "channel",
      "identifier",
      "name"
    ],
    "metrics": [
      ""
    ],
    "pagingSpec": {
      "pagingIdentifiers": {},
      "threshold": 10000
    }
  }
  """