<!DOCTYPE html>
<html>

    <header style="text-align: center;position: sticky;padding-top: 10px;">

        <h1>WeatherDrop</h1>

        <p>_______________________________________________________________________________________________________________________________________________________________</p>

        

    </header>



    <body style="background-color: lightblue;">

        <button id="5dayforecast" style="height: 40px;position: relative;background-color: transparent;color: white;border: none;cursor: pointer;font-size: medium;font-weight: bold;">
            Get the temperature for the next 5 days

        </button>

        <p id="5daytemp"></p>
      

        <div style="margin-left: 520px;margin-top: 50px;display: flex;gap: 10px;align-items: center;position: relative;">

            <input id="cityInput" placeholder="New York" style="border-radius: 5px;width: 200px;padding: 5px;height: 30px;">

           

            <button id="weather" style="border: none;cursor: pointer;width: 40px;background-color: lightblue;">
                  <img src="Search Icon.png" style="width: 60px;">
            </button>
          
        </div>

         

         <div style="width: 400px;height: 400px;border-radius: 5px;padding: 5px; box-shadow: 5px 5px 10px 2px rgba(0, 0, 0, 0.3);background-color: white;
           margin: auto;margin-top: 60px;align-items: center;">

            <img id="weathericon" style="margin-left: 150px;">
            
            
            <p id="temp" style="font-size: 40px;margin-left: 150px;"></p>

            <p id="name" style="font-size: large;font-weight: bold;margin-left: 150px;"></p>
            <p id="humidity" style="font-size: 20px;margin-left: 150px;"></p>
            <p id="speed" style="font-size: 20px;margin-left: 150px;"></p>
            <p id="condition" style="margin-left: 150px;font-size: 20px;"></p>

         </div>

         

    </body>


    <script>

      


        const fetchweather = document.getElementById('weather')
        const forecast = document.getElementById('5dayforecast')
        

        forecast.addEventListener('click', function() {
            const city = document.getElementById('cityInput').value;
           

            fetch(`https://api.openweathermap.org/data/2.5/forecast?q=${city}&appid=cccd4f6f5e38ae57702d5cd7e5addd28&units=metric`)
            .then(response => response.json())
            .then(data => {
                data.list[0].main.temp

                let output = "";

                data.list.forEach(item => {
                    if(item.dt_txt.includes("18:00:00")) {

                        output += 
                            `${item.dt_txt}${item.main.temp}<br>`

                    }
                   
                }

                )

                document.getElementById("5daytemp").innerHTML = output;
                  
                  })
            })
        
    
        
       
        fetchweather.addEventListener('click', function() {
            const city = document.getElementById('cityInput').value;
            

            fetch(`https://api.openweathermap.org/data/2.5/weather?q=${city}&appid=cccd4f6f5e38ae57702d5cd7e5addd28&units=metric`)
            .then(response => response.json())
            .then(data => {
                document.getElementById('temp').innerText = `${Math.round(data.main.temp)}°C`
                document.getElementById('name').innerText = `${data.name}` 
                document.getElementById('humidity').innerText = `Humidity:${data.main.humidity}%`
                document.getElementById('speed').innerText = `Wind:${data.wind.speed}m/s`
                document.getElementById('condition').innerText = `${data.weather[0].main}`
                document.getElementById('weathericon').src = `https://openweathermap.org/img/wn/${data.weather[0].icon}@2x.png`


                
                   
            })


            
        }) 


    </script>


</html>

