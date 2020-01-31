using Microsoft.Owin;
using Owin;

[assembly: OwinStartupAttribute(typeof(annorum_supra.Startup))]
namespace annorum_supra
{
    public partial class Startup
    {
        public void Configuration(IAppBuilder app)
        {
            ConfigureAuth(app);
        }
    }
}
