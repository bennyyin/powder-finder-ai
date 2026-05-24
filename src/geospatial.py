def calculate_driving_hours(lat1, lon1, lat2, lon2):
    """
    Calculates the estimated driving time in hours between two GPS coordinates.
    
    Args:
        lat1 (float): Latitude of the starting location.
        lon1 (float): Longitude of the starting location.
        lat2 (float): Latitude of the destination.
        lon2 (float): Longitude of the destination.

    Returns:
        float: The driving duration in hours. 
               Returns None if no driving route is found.
    """
    result = gmaps.distance_matrix(
        origins=(lat1, lon1), destinations=(lat2, lon2), mode="driving")    
    return result["rows"][0]["elements"][0]["duration"]["value"] / 3600  # Convert seconds to hours