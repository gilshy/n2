from flask import Flask, render_template, request


app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def main():
    nums = request.form.get('nums')
    res = None
    if nums:
        nums = nums.split()
        nums = list(map(int, nums))
        for num in range(1, len(nums)):
            print(nums[num - 1] - nums[num])
            if nums[num] > 0:
                if nums[num] - nums[num - 1] > 1:
                    res = nums[num] - 1
            elif nums[num] == 0:
                if nums[num - 1] != -1:
                    res = -1
            else:
                if nums[num] - nums[num - 1] > 1:
                    res = nums[num - 1] + 1
        if res is None:
            res = 'Неверно введена последовательность'
    else:
        res = 'Вы не ввели данные'
    return render_template('index.html', res=res)


if __name__ == '__main__':
    app.run(debug=True)