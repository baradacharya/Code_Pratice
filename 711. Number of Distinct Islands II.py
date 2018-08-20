"""
Approach #1: Canonical Hash [Accepted]
Intuition
As in Approach #1 to the sister problem Number of Distinct Islands, we determine local coordinates for each island.
Afterwards, we will rotate and reflect the coordinates about the origin
and translate the shape so that the bottom-left-most coordinate is (0, 0).
At the end, the smallest of these lists coordinates will be the canonical representation of the shape.

Algorithm

1. We start with the code from the previous problem, Number of Distinct Islands.
2. For each of 8 possible rotations and reflections of the shape,
we will perform the transformation and then translate the shape so that the bottom-left-most coordinate is (0, 0).
3. Afterwards, we will consider the canonical hash of the shape to be the maximum of these 8 intermediate hashes.

In Python, the motivation to use complex numbers is that rotation by 90 degrees
is the same as multiplying by the imaginary unit, 1j. In Java, we manipulate the coordinates directly.
The 8 rotations and reflections of each point are (x, y), (-x, y), (x, -y), (-x, -y), (y, x), (-y, x), (y, -x), (-y, -x).
T: O(R*C log(R * C))
S: O(R*C)
"""
class Solution(object):
    def numDistinctIslands2(self, grid):
        seen = set()
        def explore(r, c):
            if (0 <= r < len(grid) and 0 <= c < len(grid[0]) and grid[r][c] and (r, c) not in seen):
                seen.add((r, c))
                shape.add(complex(r, c))
                explore(r+1, c)
                explore(r-1, c)
                explore(r, c+1)
                explore(r, c-1)

        def canonical(shape):
            def translate(shape):
                w = complex(min(z.real for z in shape), min(z.imag for z in shape))
                return sorted(str(z-w) for z in shape)

            ans = None
            for k in xrange(4):
                ans = max(ans, translate([z * (1j)**k for z in shape]))
                ans = max(ans, translate([complex(z.imag, z.real) * (1j)**k for z in shape]))
            return tuple(ans)

        shapes = set()
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                shape = set()
                explore(r, c)
                if shape:
                    shapes.add(canonical(shape))

        return len(shapes)