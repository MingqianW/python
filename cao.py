import numpy as np

def generate_random_points(num_points, dimensions):
    """
    生成指定数量和维度的随机点
    """
    return np.random.rand(num_points, dimensions)

def compute_distances(points):
    """
    计算所有点对之间的距离
    """
    num_points = points.shape[0]
    distances = np.zeros((num_points, num_points))
    for i in range(num_points):
        for j in range(i + 1, num_points):
            distances[i, j] = np.linalg.norm(points[i] - points[j])
            distances[j, i] = distances[i, j]
    return distances

def max_distance(points):
    """
    计算所有点对之间的最大距离
    """
    distances = compute_distances(points)
    return np.max(distances)

def max_distance_to_center(points):
    """
    计算每个点到中心点（平均点）的最大距离
    """
    center = np.mean(points, axis=0)
    distances_to_center = np.linalg.norm(points - center, axis=1)
    return np.max(distances_to_center)

# 参数设置
num_points = 100  # 点的数量
dimensions = 3    # 点的维度

# 生成随机点
points = generate_random_points(num_points, dimensions)

# 计算最大点对距离和最大中心点距离的两倍
max_point_distance = max_distance(points)
max_center_distance = max_distance_to_center(points)
approx_distance = 2 * max_center_distance

print(f"最大点对距离: {max_point_distance}")
print(f"最大中心点距离的两倍: {approx_distance}")
print(f"两者之差: {(max_point_distance - approx_distance)}")
print(f"两者之差百分比: {abs(max_point_distance - approx_distance) / max_point_distance }")
