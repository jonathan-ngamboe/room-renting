import api from "@/services/api";

const endpoint = '/properties';

const propertyService = {

  getPropertyById(id) {
    return api.get(`${endpoint}/${id}`)
      .then(response => response.data)
      .catch(error => {
        throw new Error(`Failed to fetch room with ID ${id}: ` + error.message);
      });
  },

  getFilteredProperties(searchCriteria, filters) {
    const params = {
      destination: searchCriteria.destination,
      checkIn: searchCriteria.checkIn,
      checkOut: searchCriteria.checkOut,
      minPrice: filters.priceRange.min,
      maxPrice: filters.priceRange.max !== Infinity ? filters.priceRange.max : 999999,      amenities: filters.amenities.join(','),
      average_rating: filters.rating.min,
    };

    console.log("Filters params: ", params);
    
    return api.get(endpoint, { params })
      .then(response => response.data)
      .catch(error => {
        throw new Error(`Failed to fetch filtered properties: ` + error.message);
      });
  },

  // Method to add a new property
  addProperty(propertyData) {
    const data = {
      title: propertyData.title,
      description: propertyData.description,
      address: propertyData.address,
      city: propertyData.city,
      price_per_night: propertyData.price_per_night,
      surface: propertyData.surface,
      amenities: propertyData.amenities,  
      property_Type: propertyData.property_Type,
      images: propertyData.images,  
      is_active: propertyData.is_active,
      owner: propertyData.owner, 
    };

    return api.post('properties/', data)
      .then(response => response.data)
      .catch(error => Promise.reject(error.response.data));
  },
  
  // Method to retrieve property data
  getProperties() {
    return api.get('properties/')
      .then(response => response.data)
      .catch(error => Promise.reject(error.response.data));
  },

  // Method to retrieve the details of a specific property
  getPropertyDetails(propertyId) {
    return api.get(`properties/${propertyId}/`)
      .then(response => response.data)
      .catch(error => Promise.reject(error.response.data));
  },

  // Method for updating the data of an existing property
  updateProperty(propertyId, propertyData) {
    const data = {
      title: propertyData.title,
      description: propertyData.description,
      address: propertyData.address,
      city: propertyData.city,
      price_per_night: propertyData.price_per_night,
      surface: propertyData.surface,
      amenities: propertyData.amenities,  
      property_Type: propertyData.property_Type,
      images: propertyData.images,  
      is_active: propertyData.is_active,
      
    };

    return api.put(`properties/${propertyId}/`, data)
      .then(response => response.data)
      .catch(error => Promise.reject(error.response.data));
  },

  // Method to delete a property
  deleteProperty(propertyId) {
    return api.delete(`properties/${propertyId}/`)
      .then(response => response.data)
        .catch(error => Promise.reject(error.response.data));
    },
};

export default propertyService;
