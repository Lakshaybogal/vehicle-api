## Vehicle Management API

This API allows you to manage vehicle data, including uploading vehicle information and images, retrieving vehicle details, and searching for vehicles by various criteria.

### Base URL

```
https://vehicle-api-u9p7.onrender.com
```

### Endpoints

---

### Get All Vehicles

#### `GET /vehicle/getAll/`

Retrieves information about all vehicles.

#### Response

Returns a list of dictionaries containing vehicle details.

---

### Get Vehicle by ID

#### `GET /vehicle/{vehicle_id}`

Retrieves information about a specific vehicle by its ID.

#### Path Parameters

-   `vehicle_id` (str): The unique identifier of the vehicle.

#### Response

Returns a dictionary containing details of the requested vehicle.

---

### Get Vehicles by Brand

#### `GET /vehicle/brand/{brand}`

Retrieves information about vehicles by brand.

#### Path Parameters

-   `brand` (str): The brand name of the vehicles to retrieve.

#### Response

Returns a dictionary containing a list of vehicles and their count.

---

### Get Vehicles by Type

#### `GET /vehicle/type/{vehicle_type}`

Retrieves information about vehicles by type.

#### Path Parameters

-   `vehicle_type` (str): The type of vehicles to retrieve.

#### Response

Returns a dictionary containing a list of vehicles and their count.

---

### Search Vehicles by Model Name

#### `GET /vehicle/search/model/{vehicle_model}`

Searches for vehicles by their model names.

#### Path Parameters

-   `vehicle_model` (str): The partial or full name of the vehicle model to search for.

#### Response

Returns a dictionary containing a list of matching vehicles and their count.

---

### Get Vehicle Image

#### `GET /vehicle/image/{shortURL}`

Retrieves the image of a vehicle by its shortened URL.

#### Path Parameters

-   `shortURL` (str): The shortened URL of the vehicle image.

#### Response

Returns the vehicle image in the specified format (JPEG, PNG, etc.).

---

### Notes

-   All endpoints support CORS headers for cross-origin requests.
-   Errors are returned with appropriate HTTP status codes and error messages.

---

This API provides functionalities to manage vehicle data efficiently. Please refer to the provided endpoints for detailed usage instructions.
