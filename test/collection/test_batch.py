import uuid
from weaviate.collections.classes.batch import BatchObjectReturn, MAX_STORED_RESULTS


def test_batch_object_return_add() -> None:
    lhs_uuids = [uuid.uuid4() for _ in range(MAX_STORED_RESULTS - 1)]
    lhs = BatchObjectReturn(
        all_responses=lhs_uuids,
        elapsed_seconds=0.1,
        errors={},
        has_errors=False,
        uuids={idx: v for idx, v in enumerate(lhs_uuids)},
    )
    rhs_uuids = [uuid.uuid4() for _ in range(2)]
    rhs = BatchObjectReturn(
        all_responses=rhs_uuids,
        elapsed_seconds=0.1,
        errors={},
        has_errors=False,
        uuids={idx: v for idx, v in enumerate(rhs_uuids)},
    )
    result = lhs + rhs
    assert len(result.all_responses) == MAX_STORED_RESULTS
    assert len(result.uuids) == MAX_STORED_RESULTS
    assert result.uuids == {
        idx + 1: v for idx, v in enumerate(lhs_uuids[1 : MAX_STORED_RESULTS - 1] + rhs_uuids)
    }
