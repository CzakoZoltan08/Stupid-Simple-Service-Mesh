namespace service5.Controllers
{
    using Microsoft.AspNetCore.Mvc;

    [ApiController]
    [Route("[controller]")]
    public class GreeterController : ControllerBase
    {
        [HttpGet]
        public string Get()
        {
            return "Hello from .Net";
        }
    }
}
