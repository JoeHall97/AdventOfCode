local function puzzle_two()
    local total = 0
    local numWord = {
        ["one"]=1,
        ["two"]=2,
        ["three"]=3,
        ["four"]=4,
        ["five"]=5,
        ["six"]=6,
        ["seven"]=7,
        ["eight"]=8,
        ["nine"]=9
    }
    for line in io.lines('puzzle.txt') do
        local first, last = 0, 0
        for i = 0, #line do
            if string.find(line:sub(i, i), "%d") ~= nil then
               if first == 0 then
                    first = tonumber(line:sub(i, i), 10)
               end
               last = tonumber(line:sub(i, i), 10)
            else
                for word, num in pairs(numWord) do
                    if i + word:len() - 1 > line:len() then
                        goto continue
                    end
                    if word == line:sub(i, i + word:len() - 1) then
                        if first == 0 then
                            first = num
                        end
                        last = num
                        i = i + word:len() - 1
                        break
                    end
                    ::continue::
                end
            end
        end
        total = total + (first * 10) + last
    end
    print(total)
end

local function puzzle_one()
    local total = 0
    for line in io.lines('puzzle.txt') do
        local first = string.match(line, "%d")
        local last = string.match(string.reverse(line), "%d")
        total = total + tonumber(first .. last)
    end
    print(total)
end

puzzle_one()
puzzle_two()