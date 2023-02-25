import pytest
from task_1 import geo_logs, unique_list_id, max_, stats

if __name__ == '__main__':
    #тест к заданию 1
    @pytest.mark.parametrize("x", geo_logs)
    def test_visits_from_russia(x):
        country = list(x.values())[0][1]
        assert country == 'Россия'


    #тест к заданию 2
    @pytest.mark.parametrize('x', unique_list_id)
    def test_unique_id(x):
        assert unique_list_id.count(x) == 1


    #тест к заданию 4
    def test_max_stats():
        assert stats[max_] == max(stats.values())