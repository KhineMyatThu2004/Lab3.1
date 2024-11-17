import price_info as tt
def test_total_cost_shopping():
  
    result=tt.total_cost_shopping()
    test_result=46.75
    assert result==test_result

def test_cost_of_fruit():
    
    result=tt.cost_of_fruits('apple',10)
    assert result==12