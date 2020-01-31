using Microsoft.Owin;
using Owin;

[assembly: OwinStartupAttribute(typeof(allpax_sale_miner.Startup))]
namespace allpax_sale_miner
{
    public partial class Startup
    {
        public void Configuration(IAppBuilder app)
        {
            ConfigureAuth(app);
        }
    }
}
