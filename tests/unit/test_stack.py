from src.stack import Stack
import pytest

class TestStack:
    
    @pytest.mark.parametrize("list_of_values", [[1,2,3,4,5000]])
    def test_push(self,list_of_values):
        ## Arrange
        st = Stack()

        ## Act
        st.push_all(list_of_values)

        ## Assert   
        assert st.get_stack_size() == 5
        assert st.get_peek() == 5000
        assert st.is_empty() == False
        assert st.get_current_stack() == list_of_values

        ## Act 
        res = st.pop()
        assert res == 5000
        assert st.get_stack_size() == 4
        assert st.get_peek() == 4
        assert st.is_empty() == False
        assert st.get_current_stack() == [1,2,3,4]


    def test_pop(self):
        ## Arrange
        st = Stack()

        ## Act
        st.push_all([1,2,3,4,5000,10000,20000])

        ## Assert   
        assert st.get_stack_size() == 7
        assert st.get_peek() == 20000
        assert st.is_empty() == False
        assert st.get_current_stack() == [1,2,3,4,5000,10000,20000]

        ## Act 
        res = st.pop()
        assert res == 20000
        assert st.get_stack_size() == 6
        assert st.get_peek() == 10000
        assert st.is_empty() == False
        assert st.get_current_stack() == [1,2,3,4,5000,10000]

        ## Act
        res = st.pop()
        assert res == 10000
        assert st.get_stack_size() == 5
        assert st.get_peek() == 5000
        assert st.is_empty() == False
        assert st.get_current_stack() == [1,2,3,4,5000]

        ## Act 
        st.clear_stack()
        assert st.get_stack_size() == 0
        assert st.is_empty() == True
        assert st.get_current_stack() == []




