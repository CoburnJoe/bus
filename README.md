# Bus - Python Json Aggregator
Pre-Alpha project

Takes json payloads and combines them by nesting one in the payload of another using a shared key.

## Installation

Install with Pip:

```bash
pip install bus
```

## Usage

```python
from bussing.busses import Bus
Bus().group(parent='PARENT JSON', child='CHILD JSON', keys=[("id", "shapes")]
```

Keys needs to be a list of tuples. The first element is the key ID to match results with,
and the second is the new name to list items as under the parent.

## Examples

Given:

```json
[
   {
      "id":"Apples",
      "colours":[
         "Red",
         "Green"
      ]
   },
   {
      "id":"Bananas",
      "colours":[
         "Yellow"
      ]
   },
   {
      "id":"Mangos",
      "colours":[
         "Orange",
         "Green"
      ]
   }
]
```

And:

```json
[
   {
      "id":"Apples",
      "round":true
   },
   {
      "id":"Bananas",
      "round":false
   }
]
```

You can combine these results into one payload:

```json
[
   {
      "id":"Apples",
      "colours":[
         "Red",
         "Green"
      ],
      "shapes":{
         "round":true
      }
   },
   {
      "id":"Bananas",
      "colours":[
         "Yellow"
      ],
      "shapes":{
         "round":false
      }
   },
   {
      "id":"Mangos",
      "colours":[
         "Orange",
         "Green"
      ]
   }
]
```

