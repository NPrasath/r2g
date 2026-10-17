var builder = WebApplication.CreateBuilder(args);
var app = builder.Build();

app.MapGet("/", () => Results.Ok(new
{
    name = "R2G AI-assisted SDLC training",
    stage = "starter",
    businessModulesImplemented = false
}));

app.MapGet("/health", () => Results.Ok(new { status = "ok" }));

app.Run();

// Make the generated entry point available to the integration test host.
public partial class Program { }
