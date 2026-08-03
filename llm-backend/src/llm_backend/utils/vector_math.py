import math


class VectorMath:

    @staticmethod
    def dimension(
        embedding: list[float],
    ) -> int:
        return len(embedding)

    @staticmethod
    def norm(
        embedding: list[float],
    ) -> float:
        return math.sqrt(
            sum(x * x for x in embedding)
        )

    @staticmethod
    def dot(
        a: list[float],
        b: list[float],
    ) -> float:

        if len(a) != len(b):
            raise ValueError("벡터의 차원이 일치하지 않습니다.")

        return sum(x * y for x, y in zip(a, b))

    @staticmethod
    def cosine_similarity(
        a: list[float],
        b: list[float],
    ) -> float:

        if len(a) != len(b):
            raise ValueError("벡터의 차원이 일치하지 않습니다.")

        norm_a = VectorMath.norm(a)
        norm_b = VectorMath.norm(b)

        if norm_a == 0 or norm_b == 0:
            raise ValueError("벡터의 노름이 0입니다.")

        return VectorMath.dot(a, b) / (norm_a * norm_b)