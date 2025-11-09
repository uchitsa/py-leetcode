type TwoSum struct {
    nums []int
    sorted bool
}


func Constructor() TwoSum {
    return TwoSum{nums: []int{}, sorted: false}
}


func (this *TwoSum) Add(number int)  {
    this.nums = append(this.nums, number)
    this.sorted = false
}


func (this *TwoSum) Find(value int) bool {
    if !this.sorted {
        sort.Ints(this.nums)
        this.sorted = true
    }
    lo, hi := 0, len(this.nums)-1
    for lo<hi {
        sum2 := this.nums[lo]+this.nums[hi]
        if sum2<value {
            lo++
        } else if sum2 > value {
            hi--
        } else {
            return true
        }
    }
    return false
}


/**
 * Your TwoSum object will be instantiated and called as such:
 * obj := Constructor();
 * obj.Add(number);
 * param_2 := obj.Find(value);
 */
