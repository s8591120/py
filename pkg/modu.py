def triangle_zhonxin(a, b, c):
    """
    Calculate the centroid (重心) of a triangle.

    Parameters:
    - a (tuple): Coordinates of point A (x1, y1).
    - b (tuple): Coordinates of point B (x2, y2).
    - c (tuple): Coordinates of point C (x3, y3).

    Returns:
    tuple: Coordinates of the centroid G (x, y).

    Example:
    >>> triangle_zhonxin((1, 1), (2, 2), (3, 3))
    (2, 2)
    """
    x = round((a[0] + b[0] + c[0]) / 3)
    y = round((a[1] + b[1] + c[1]) / 3)
    return x, y
